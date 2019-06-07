Title: Frequent pattern mining - Apriori
Date: 2019-01-10
Category: Machine Learning
Tags: machine learning, frequent pattern mining

Apriori(*I don't kown how to pronounce...*) is an algorithm for frequent pattern mining. Frequent pattern mining is an important problem in data mining, like cart analysis, etc. Apriori algorhtm mainly focused on mining frequent pattern in transactional database.

Enough with all the chitchat, let's discuss Apriori in detail. Apriori is not a complicated algorithm, it's pretty straightforward and anyone with basic math knowledge can understand it well. [Wikipedia](https://en.wikipedia.org/wiki/Apriori_algorithm) did a pretty good and detailed introduction. However in it introduced a lot of notations, for someone not that into math notations(*like me*), it's easy to forget what they stands for and shortly I won't remember all the details. That's the reason I'm writing this article, I hope I can have a deep understand about it and if someday I need to re-learn it, I can pick it up easily from here.

### Problem

Quote from wikipedia:

> The following is a formal statement of the problem: Let $\tau=\{i_{1},i_{2},...,i_{m}\}$ be a set of literals, called items. Let $D$ be a set of transactions, where each transaction $T$ is a set of items such that $T\subseteq\tau$. Associated with each transaction is a unique identifier, called its $TID$. We say that a transaction $T$ contains $X$, a set of some items in $\tau$, if $X⊆T$. An association rule is an implication of the form $X⇒Y$ , where $X\subset\tau$, $Y\subset\tau$, and $X∩Y=∅$. The rule $X⇒Y$ holds in the transaction set $D$ with confidence $c$ if $c%$ of transactions in D that contain $X$ also contain $Y$ . The rule $X⇒Y$ has support $s$ in the transaction set $D$ if $s%$ of transactions in $D$ contain $X∪Y$. Given a set of transactions $D$, the problem of mining association rules is to generate all association rules that have support and confidence greater than the user-specified minimum support (called minsup) and minimum confidence (called minconf) respectively.

Well... that's a lot of notations, but if you read it in detail, it's all about some basic set operations and not that hard to understand, except the part about association rules - it did make me confuse when I first read about. Here, I'm going to use an example to help understand it. Suppose now we have a list of customer orers from some shopping website stored in databse, and each order may contain one or more items which customers bought. Each order can be indetified with a unique id, and each item are identified with a number as it's unique id. Records in database is as following.

Order ID|Items
---|:--:
O1|1,2,3,4
O2|1,2,4
O3|1,2
O4|2,3,4
O5|2,3
O6|3,4
O7|2,4

The whole database represented with above table is notated as $D$ in problem definition, which contains all the customer orders in our example. Each record in the database, aka each row in above table, is a transaction, notated $T$, and uniquely identified with $TID$, which is $O1,O2,...$ . The whole item set $\tau$ in our example is $\{1,2,3,4\}$. What we need to do is to find out some subsets of $\tau$ so that they are frequently bought together by customers. The "frequently bought together" is defined with support value, means that how many transactions in the database contains the subset, aka how many orders contains the subitems. For example, we want to find items that are bought together 3 times or above, here the 3 is the support value.

### Naive Solution

The first solution of above problem comes to my mind would be: first get all the subsets of itemset, and then filter out those which not met support value condition. For our example above, with itemset $\{1,2,3,4\}$, all the subsets are: $\{\{1\},\{2\},\{3\},\{4\},\{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\},\{1,2,3\},\{1,2,4\},\{2,3,4\},\{1,2,3,4\}\}$. Then, we scan the database to see which subsets are not qualified, filter out those and we got our answer. We already introduced how to [find the powerset](/interview-question-powerset.html) in previous post. See pesudo code for this solution as below:

```python
findFrequentPatterns(database, support):
    result = empty set
    itemSet = empty set
    for transaction in database:
        add items into itemset
    powerSet = findPowerSet(itemSet)
    for subset in powerSet:
        count = 0
        for transaction in database:
            if transaction contains subset:
                count += 1
        if count >= support:
            add subset into result
    return result
```

Now we can see that this is not a perfect solution, because we need to scan database $O(2^n)$ times (which is the size of powerset), with $n$ as the size of item set. In real scenario this is absolutely not acceptable.

### Corollaries

Now let's look back at the naive solution, what makes it so bad that we can't accept? Probably the $O(2^n)$ times database scan. In order to find out which subsets are not qualified, we have to check each one with all the transactions. But wait, do we have to check all the subsets? How can we reduce the count of subsets we have to check?

This lead to the corollaries we will introduce in this section. They are very simple, but I'm not a smart guy, so I will still explain in detail. Now, as reluctant as I am, I still need to introduce some notations to make it easier for me to explain everything:

Let $X$, $Y$ be subsets of itemset, aka $X\subseteq\tau$, and $Y\subseteq\tau$, where $\tau$ is the whole item set. **Observe that if $X\subseteq Y$, then $sup(X) \ge sup(Y)$, where $sup(X)$ means the support value of set $X$**. This is pretty obvious, as $X$ is subset of $Y$, $X$ must contain the same or less items than $Y$, so we can't expect more occurrence of $Y$ then $X$ in $D$, which means $sup(X) \ge sup(Y)$. This lead to following corollaries:

* If $X$ is frequent, then any subset $Y \subseteq X$ is also frequent.
* If $X$ is not frequent, then any superset $Y \supseteq X$ can not be frequent.

This really helped us. Remember, we are suffering from two many subsets need to be checked, but with above rules, we can get the result but check less subsets, therefore, the solution now maybe eligible for real scenarios.

### Two Sub-problems

### Apriori Algorithm

### References

* [Apriori algorithm on wikipedia](https://en.wikipedia.org/wiki/Apriori_algorithm)
* [SPMF: An Open-Source Data Mining Library](https://www.philippe-fournier-viger.com/spmf/index.php)
* [Fast Algorithms for Mining Association Rules](https://www.philippe-fournier-viger.com/spmf/apriori_longer.pdf)
