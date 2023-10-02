echo hello
termux-vibrate
question=$(termux-clipboard-get)
cd /data/data/com.termux/files/home/ChatGPT_termux
echo $question
python chat-gpt.py -q ${question}
cat /data/data/com.termux/files/home/ChatGPT_termux/result.txt | termux-clipboard-set
