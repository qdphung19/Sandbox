from flask import render_template, request, Blueprint, redirect, flash
from models.backup import BackupFile

backup_view = Blueprint('backup', __name__, template_folder='templates')

@backup_view.route('/backup', methods=["POST", "GET"])
def backup_db():
    BackupFile.backup(9)
    return 'DB Backed up'

@backup_view.route('/restore/<time>', methods=['GET'])
def restore_db(time):
    BackupFile.restore(time)
    return 'DB restored'