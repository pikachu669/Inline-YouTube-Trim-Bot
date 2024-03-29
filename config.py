#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("API_ID", '28361260'))
    API_HASH = os.environ.get("API_HASH", "38c131498b9cdeacde8f1f763d466840")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7134410001:AAH3yecgCvxiCm5JpZs76iLBeU1OW12X1TE")     
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1002068157366'))
