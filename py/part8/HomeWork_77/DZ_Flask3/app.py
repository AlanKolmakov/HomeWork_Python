import os.path

from flask import Flask
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "fl_dz3.db")))