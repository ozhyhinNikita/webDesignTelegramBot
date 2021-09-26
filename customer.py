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


class Customer:
    def __init__(self):
        self.customer_id = 0
        self.name = " "
        self.service = " "

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_service(self, service):
        self.service = service

    def get_service(self):
        return self.service

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id
