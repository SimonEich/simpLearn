import sqlite3

class DB:
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn_db()
        self.create_db()
        
    def conn_db(self) -> None:
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
    def create_db(self) -> None:
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS words (
                id_words INTEGER PRIMARY KEY AUTOINCREMENT,
                word VARCHAR NOT NULL,
                translation VARCHAR NOT NULL,
                sentence TEXT
                
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS statistic (
                id_statistic INTEGER PRIMARY KEY AUTOINCREMENT,
                word_id INTEGER UNIQUE,
                right INTEGER DEFAULT 0,
                wrong INTEGER DEFAULT 0,
                state BOOL DEFAULT FALSE,
                FOREIGN KEY (word_id) REFERENCES words(id_words) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()
        
        
    def print_all_words_with_statistics(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT w.word, w.translation, w.sentence, s.right, s.wrong, s.state
            FROM words w
            JOIN statistic s ON w.id_words = s.word_id
        ''')
        rows = cursor.fetchall()

        # Print header
        print(f"{'Word':<15} | {'Translation':<15} | {'Sentence':<30} | {'Right':<5} | {'Wrong':<5} | {'State':<5}")
        print("-" * 90)

        # Print each row
        for word, translation, sentence, right, wrong, state in rows:
            print(f"{word:<15} | {translation:<15} | {sentence[:30]:<30} | {right:<5} | {wrong:<5} | {str(state):<5}")

    def statistic(self)->list:

        # Total number of words
        self.cursor.execute('SELECT COUNT(*) FROM words')
        total_words = self.cursor.fetchone()[0]

        # Words with right > 12
        self.cursor.execute('''
            SELECT w.word, w.translation, w.sentence, s.right
            FROM words w
            JOIN statistic s ON w.id_words = s.word_id
            WHERE s.right >= 12
        ''')
        words_with_high_right = len(self.cursor.fetchall())

        # Number of words with state = TRUE
        self.cursor.execute('SELECT COUNT(*) FROM statistic WHERE state = TRUE')
        num_state_true = self.cursor.fetchone()[0]
        
        print(f'Words with number Higher 12 right : {words_with_high_right}')

        return total_words, words_with_high_right, num_state_true

    def add_word(self, word, translation):
        self.cursor.execute(
            '''INSERT INTO words (word, translation) VALUES (?, ?)''',
            (word, translation)
        )
        word_id = self.cursor.lastrowid
        self.cursor.execute(
            '''INSERT INTO statistic (word_id) VALUES (?)''',
            (word_id,)
        )
        self.conn.commit()
        
    def add_listdata_db(self, file_path: str) -> None:
        
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue

                # Split line into components
                try:
                    word, translation, sentence = [part.strip() for part in line.strip().split(":", 2)]
                except ValueError:
                    print(f"Skipping malformed line: {line}")
                    continue

                # Insert into words table
                cursor = self.conn.cursor()
                cursor.execute('''
                    INSERT INTO words (word, translation, sentence)
                    VALUES (?, ?, ?)
                ''', (word, translation, sentence))

                word_id = cursor.lastrowid

                # Insert default statistics row
                cursor.execute('''
                    INSERT INTO statistic (word_id)
                    VALUES (?)
                ''', (word_id,))

            self.conn.commit()
            
    def states_to_true(self, number: int) -> None:
        cursor = self.conn.cursor()

        # Select word_ids of 'number' random words with state = FALSE
        cursor.execute('''
            SELECT word_id FROM statistic
            WHERE state = FALSE
            ORDER BY RANDOM()
            LIMIT ?
        ''', (number,))

        word_ids = [row[0] for row in cursor.fetchall()]

        # Update state to TRUE for those word_ids
        cursor.executemany('''
            UPDATE statistic
            SET state = TRUE
            WHERE word_id = ?
        ''', [(word_id,) for word_id in word_ids])

        self.conn.commit()
        print(f"Updated {len(word_ids)} words to state = TRUE")

                       
            
    def get_randomWords(self, number: int)->None:
        cursor = self.conn.cursor()
        cursor.execute('''
                SELECT w.word, w.translation, w.sentence
                    FROM words w
                    JOIN statistic s ON w.id_words = s.word_id
                    WHERE s.state = FALSE
                    ORDER BY RANDOM()
                    LIMIT ?

                        ''', (number,))
        rows = cursor.fetchall()
        
        
    def get_all_tue_state(self) -> list[tuple[str, str, str]]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT w.id_words, w.word, w.translation, w.sentence, s.right, s.wrong
            FROM words w
            JOIN statistic s ON w.id_words = s.word_id
            WHERE s.state = TRUE AND s.right < 12
        ''')
        return cursor.fetchall()
                     

    def has_any_true_state(self) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 1 FROM statistic
            WHERE state = TRUE
            LIMIT 1
        ''')
        result = cursor.fetchone()
        return result is not None



    def print_all_words_and_stats(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT w.id_words, w.word, w.translation, w.sentence,
                   s.right, s.wrong, s.state
            FROM words w
            LEFT JOIN statistic s ON w.id_words = s.word_id
            ORDER BY w.id_words
        ''')
        rows = cursor.fetchall()

        #for row in rows:
        #    id_words, word, translation, sentence, right_count, wrong_count, state = row
        #    print(f"ID: {id_words}")
        #    print(f"  Word: {word}")
        #    print(f"  Translation: {translation}")
        #    print(f"  Sentence: {sentence}")
        #    print(f"  Correct answers: {right_count if right_count is not None else 0}")
        #    print(f"  Wrong answers: {wrong_count if wrong_count is not None else 0}")
        #    print(f"  State: {bool(state)}")
        #    print("-" * 40)

    def training_right(self, word_id: int) -> None:
        print('training right')
        cursor = self.conn.cursor()

        cursor.executemany('''
            UPDATE statistic
            SET right = right + 1
            WHERE word_id = ?
        ''', [(word_id, )])

        self.conn.commit()

        # Fetch both word_id and right count
        cursor.execute('''
            SELECT word_id, right FROM statistic
            WHERE right > 0
        ''')
        

        rows = cursor.fetchall()
        
    def training_right_rep(self, word_id: int) -> None:
        print('training right')
        cursor = self.conn.cursor()

        cursor.executemany('''
            UPDATE statistic
            SET wrong = wrong - 1
            WHERE word_id = ?
        ''', [(word_id, )])

        self.conn.commit()

        # Fetch both word_id and right count
        cursor.execute('''
            SELECT word_id, wrong FROM statistic
            WHERE right > 0
        ''')
        

        rows = cursor.fetchall()
        
        print('Words in the Game: ' + str(len(rows)))
        for word_id, right in rows:
            print(f"{word_id} {right} ")


        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
            
    def training_wrong(self, word_id:int) -> None:
        print('trining wrong')
        cursor = self.conn.cursor()
        cursor.executemany('''
            UPDATE statistic
            SET wrong = wrong + 1
            WHERE word_id = ?
        ''', [(word_id, )])
        
        self.conn.commit()
        
        cursor.execute('''
            SELECT word_id FROM statistic
            WHERE wrong > 0
        ''')

        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
            
            
    def get_words_with_wrong_answers(self) -> list[tuple[str, str, str, int, int]]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT w.id_words, w.word, w.translation, w.sentence, s.right, s.wrong
            FROM words w
            JOIN statistic s ON w.id_words = s.word_id
            WHERE s.wrong > 0
        ''')
        return cursor.fetchall()
