# ------------------------------------------------------------------------
# Copyright 2021 Nikita Ozhyhin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------


import sqlite3


def load_db():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                id INTEGER,
                name TEXT,
                service TEXT)
                """)
    conn.commit()
    conn.close()


def insert_user(user_id, name, service):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (id, name, service) VALUES (?,?,?)",
                   (user_id, name, service))
    conn.commit()
    conn.close()
