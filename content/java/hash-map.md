Title: HashMap in JDK8
Date: 2019-01-01
Category: Java
Tags: java, hash map

HashMap is a commonly used data structure in Java development, I guess every developer would use it, well, almost every day. However we may not understand it as we should, at least I didn't put more attention on it previously. Lately I found some interview questions about HashMap which are pretty interesting, and I thought it should be a good motivation to know more about HashMap, so that I won't be blocked if challenged in an interview.

First let's raise some questions about HashMap, these are asked a lot by interviewers.

* What's the initial capacity of HashMap?
* What's the default load factor of HashMap?
* What's the data structure internally used in HashMap?
* If create HashMap with code `new HashMap<>(20)`, what the size of bucket array should be?
