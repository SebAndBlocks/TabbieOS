sudo /tabbie/web/.venv/bin/mod_wsgi-express start-server \
    /tabbie/web/app.py \
    --user hello --group hello --port 80 --processes 4
chromium-browser --kiosk http://127.0.0.1:5000