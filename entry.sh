export API_KEY="YOUR_API_KEY"

# START OF C++
g++ src/cpp/example.cpp -o code -lcurl
./code
# END OF C++

# START OF Java
java -classpath /usr/share/java/gson.jar src/java/example.java
# END OF Java

# START OF Python
python3 src/python/example.py
# END OF Python