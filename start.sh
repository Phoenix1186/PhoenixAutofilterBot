if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ph0enix_web/test1.git /PhoenixAutofilterBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PhoenixAutofilterBot
fi
cd /PhoenixAutofilterBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
