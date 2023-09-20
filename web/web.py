# Copyright 2023 RISC-V International
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
#
#           Rafael Sene <rafael@riscv.org> - Initial implementation.

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def homepage():
    # HTML file is named 'index.html' and 
    # located in a directory named 'static' 
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)