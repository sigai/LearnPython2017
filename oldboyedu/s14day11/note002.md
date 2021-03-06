#redis

简单的key-value的缓存系统.

SET key value [EX seconds] [PX milliseconds] [NX|XX]
Set the string value of a key

KEYS pattern
Find all keys matching the given pattern

SETEX key seconds value
Set the value and expiration of a key

python模块redis实现用python操作redis
(返回的都是bytes类型, python3中一切socket相关的数据都是bytes类型)
1. 操作模式
redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
2. 连接池
redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
3. 操作
- string操作
- hash操作
- list操作
- set操作
- sort set操作
4. 管道
5. 发布/订阅

#string操作:
`set(name, value, ex=None, px=None, nx=False, xx=False)`
Set the value at key ``name`` to ``value``
设置key `name` 的 value为 `value`, 成功返回True, 失败返回False.
    ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.
    `ex`参数为key `name` 设置一个超时秒数标识, 过了超时时间, key `name`会被删除. 期间会阻塞.
    ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.
    `px`参数同`ex`, 时间单位为毫秒(千分之一秒).
    ``nx`` if set to True, set the value at key ``name`` to ``value`` if it
        does not already exist.
    `nx`参数如果指定为True, 只有在`name` key不存在的情况下, 它才会被设置为`value`. 设置成功返回True, 失败返回False.
    ``xx`` if set to True, set the value at key ``name`` to ``value`` if it
        already exists.
    `xx`参数如果指定为True, 只有在`name` key存在的情况下, 它才会被设置为`value`. 设置成功返回True, 失败返回False.
`setnx(name, value)`
Set the value of key ``name`` to ``value`` if key doesn't exist
在`name` key不存在的情况下, 设置`name`的值为`value`, 返回True, 否则返回False.

`setex(name, value, time)`
    Set the value of key ``name`` to ``value`` that expires in ``time``
    seconds. ``time`` can be represented by an integer or a Python
    timedelta object.
    设置`name`的值为`value`, 有效时间为`time`秒. `time`参数可以是一个整数, 也可以是Python的timedelta对象.

`psetex(name, time_ms, value)`
    Set the value of key ``name`` to ``value`` that expires in ``time_ms``
    milliseconds. ``time_ms`` can be represented by an integer or a Python
    timedelta object.
    设置`name`的值为`value`, 有效时间为`time_ms`毫秒. `time_ms`参数可以是整数或者Python的timedelta对象.

`mset(*args, **kwargs)`
    Sets key/values based on a mapping. Mapping can be supplied as a single
    dictionary argument or as kwargs.
    根据映射关系设置键值对. 映射可以是一个简单的字典参数, 或者关键字参数.
    
`get(name)`
    Return the value at key ``name``, or None if the key doesn't exist
    返回`name`对应的值, 如果`name`不存在则返回None.

`mget(keys, *args)`
    Returns a list of values ordered identically to ``keys``
    返回所有keys参数对应的值的列表.

`getset(name, value)`
    Sets the value at key ``name`` to ``value``
    and returns the old value at key ``name`` atomically.
    设置`name`的值为`value`, 同时自动返回`name`原来的值.
    
`getrange(key, start, end)`
    Returns the substring of the string value stored at ``key``,
    determined by the offsets ``start`` and ``end`` (both are inclusive)
    返回key对应的值的子字符串. 由参数start和end决定子字符串的开始和结束, 包含两端的字符.
`setrange(name, offset, value)`
    Overwrite bytes in the value of ``name`` starting at ``offset`` with
    ``value``. If ``offset`` plus the length of ``value`` exceeds the
    length of the original value, the new value will be larger than before.
    If ``offset`` exceeds the length of the original value, null bytes
    will be used to pad between the end of the previous value and the start
    of what's being injected.
    Returns the length of the new string.
    用value的值覆盖name的对应值从offset起始位置开始替换. 如果起始位置加上value的值的长度大于原始值的长度, 最终值的长度就会边长. 如果起始位置offset超过原始值的长度, 中间将会用`null`字符填充.
    返回值为最终字符串的长度.

`setbit(name, offset, value)`
    Flag the ``offset`` in ``name`` as ``value``. Returns a boolean
    indicating the previous value of ``offset``.
    把name对应的值的二进制位的offset位标为value, 返回该位置原来的二进制值.
    用途: 把一个数据的二进制位看成一个列表, 存储序列和True和False(1和0).
    mysql一张表超过500万条数据就慢了.

`getbit(name, offset)`
    Returns a boolean indicating the value of ``offset`` in ``name``
    返回name对应的值的二进制的offset位置的二进制值的布尔值形式.

`bitcount(key, start=None, end=None)`
    Returns the count of set bits in the value of ``key``.  Optional
    ``start`` and ``end`` paramaters indicate which bytes to consider 
    返回key对应的值的二进制位中的1的个数. 可选参数可指定统计的起始位置.   

`strlen(name)`
    Return the number of bytes stored in the value of ``name``
    返回name对应值的字节长度.

`incr(name, amount=1)`
    Increments the value of ``key`` by ``amount``.  If no key exists,
    the value will be initialized as ``amount``
    把name对应的值增加amount, 如果name不存在, 初始name的值为amount.

`incrbyfloat(name, amount=1.0)`
    Increments the value at key ``name`` by floating ``amount``.
    If no key exists, the value will be initialized as ``amount``
    把name对应的值按浮点类型增加amount, 不过name不存在, 将name值初始化为amount.

`decr(name, amount=1)`
    Decrements the value of ``key`` by ``amount``.  If no key exists,
    the value will be initialized as 0 - ``amount``
    把name对应的值减少amount, 如果name不存在, name的值初始化为 0 - amount.

`append(key, value)`
    Appends the string ``value`` to the value at ``key``. If ``key``
    doesn't already exist, create it with a value of ``value``.
    Returns the new length of the value at ``key``.
    把value追加到key对应的值后面. 如果key不存在, 则创建一个值为value的key.
    返回值为key对应的新值的长度.
    
`scan(self, cursor=0, match=None, count=None)`:
        Incrementally return lists of key names. Also return a cursor indicating the scan position.
        ``match`` allows for filtering the keys by pattern
        ``count`` allows for hint the minimum number of returns

`scan_iter(self, match=None, count=None)`:
        Make an iterator using the SCAN command so that the client doesn't need to remember the cursor position.
        ``match`` allows for filtering the keys by pattern
        ``count`` allows for hint the minimum number of returns

#hash操作:
`hdel(self, name, *keys)`:
   Delete ``keys`` from hash ``name``

`hexists(self, name, key)`:
   Returns a boolean indicating if ``key`` exists within hash ``name``

`hget(self, name, key)`:
   Return the value of ``key`` within the hash ``name``

`hgetall(self, name)`:
   Return a Python dict of the hash's name/value pairs

`hincrby(self, name, key, amount=1)`:
   Increment the value of ``key`` in hash ``name`` by ``amount``

`hincrbyfloat(self, name, key, amount=1.0)`:
   Increment the value of ``key`` in hash ``name`` by floating ``amount``

`hkeys(self, name)`:
   Return the list of keys within hash ``name``

`hlen(self, name)`:
   Return the number of elements in hash ``name``

`hset(self, name, key, value)`:
   Set ``key`` to ``value`` within hash ``name``
   Returns 1 if HSET created a new field, otherwise 0

`hsetnx(self, name, key, value)`:
   Set ``key`` to ``value`` within hash ``name`` if ``key`` does not
   exist.  Returns 1 if HSETNX created a field, otherwise 0.

`hmset(self, name, mapping)`:
   Set key to value within hash ``name`` for each corresponding
   key and value from the ``mapping`` dict.

`hmget(self, name, keys, *args)`:
   Returns a list of values ordered identically to ``keys``

`hvals(self, name)`:
   Return the list of values within hash ``name``
`hscan(self, name, cursor=0, match=None, count=None)`:
       
   Incrementally return key/value slices in a hash. Also return a cursor
   indicating the scan position.

   ``match`` allows for filtering the keys by pattern

   ``count`` allows for hint the minimum number of returns

`hscan_iter(self, name, match=None, count=None)`:

   Make an iterator using the HSCAN command so that the client doesn't
   need to remember the cursor position.

   ``match`` allows for filtering the keys by pattern

   ``count`` allows for hint the minimum number of returns

#list操作:
`blpop(self, keys, timeout=0)`:
   LPOP a value off of the first non-empty list
   named in the ``keys`` list.
   If none of the lists in ``keys`` has a value to LPOP, then block
   for ``timeout`` seconds, or until a value gets pushed on to one
   of the lists.
   If timeout is 0, then block indefinitely.


`brpop(self, keys, timeout=0)`:
   RPOP a value off of the first non-empty list
   named in the ``keys`` list.
   If none of the lists in ``keys`` has a value to LPOP, then block
   for ``timeout`` seconds, or until a value gets pushed on to one
   of the lists.
   If timeout is 0, then block indefinitely.


`brpoplpush(self, src, dst, timeout=0)`:
   Pop a value off the tail of ``src``, push it on the head of ``dst``
   and then return it.
   This command blocks until a value is in ``src`` or until ``timeout``
   seconds elapse, whichever is first. A ``timeout`` value of 0 blocks
   forever.


`lindex(self, name, index)`:
   Return the item from list ``name`` at position ``index``
   Negative indexes are supported and will return an item at the
   end of the list


`linsert(self, name, where, refvalue, value)`:
   Insert ``value`` in list ``name`` either immediately before or after
   [``where``] ``refvalue``
   Returns the new length of the list on success or -1 if ``refvalue``
   is not in the list.

        
`llen(self, name)`:
        "Return the length of the list ``name``"

`lpop(self, name)`:
        "Remove and return the first item of the list ``name``"

`lpush(self, name, *values)`:
        "Push ``values`` onto the head of the list ``name``"

`lpushx(self, name, value)`:
        "Push ``value`` onto the head of the list ``name`` if ``name`` exists"

`lrange(self, name, start, end)`:
   Return a slice of the list ``name`` between
   position ``start`` and ``end``
   ``start`` and ``end`` can be negative numbers just like Python slicing notation

`lrem(self, name, count, value)`:
   Remove the first ``count`` occurrences of elements equal to ``value``
   from the list stored at ``name``.
   The count argument influences the operation in the following ways:
       count > 0: Remove elements equal to value moving from head to tail.
       count < 0: Remove elements equal to value moving from tail to head.
       count = 0: Remove all elements equal to value.

`lset(self, name, index, value)`:
        "Set ``position`` of list ``name`` to ``value``"
        
`ltrim(self, name, start, end)`:

   Trim the list ``name``, removing all values not within the slice between ``start`` and ``end``
   ``start`` and ``end`` can be negative numbers just like Python slicing notation

`rpop(self, name)`:
   "Remove and return the last item of the list ``name``"

`rpoplpush(self, src, dst)`:
   RPOP a value off of the ``src`` list and atomically LPUSH it on to the ``dst`` list.  Returns the value.

`rpush(self, name, *values)`:
   Push ``values`` onto the tail of the list ``name``

`rpushx(self, name, value)`:
   Push ``value`` onto the tail of the list ``name`` if ``name`` exists

`sort(self, name, start=None, num=None, by=None, get=None,
             desc=False, alpha=False, store=None, groups=False)`:
   Sort and return the list, set or sorted set at ``name``.
   ``start`` and ``num`` allow for paging through the sorted data
   ``by`` allows using an external key to weight and sort the items.
       Use an `*` to indicate where in the key the item value is located
   ``get`` allows for returning items from external keys rather than the
       sorted data itself.  Use an `*` to indicate where int he key
       the item value is located
   ``desc`` allows for reversing the sort
   ``alpha`` allows for sorting lexicographically rather than numerically
   ``store`` allows for storing the result of the sort into
       the key ``store``
   ``groups`` if set to True and if ``get`` contains at least two
       elements, sort will return a list of tuples, each containing the
       values fetched from the arguments to ``get``.

#set操作
`sadd(self, name, *values)`:
        Add ``value(s)`` to set ``name``

`scard(self, name)`:
        Return the number of elements in set ``name``

`sdiff(self, keys, *args)`:
        Return the difference of sets specified by ``keys``

`sdiffstore(self, dest, keys, *args)`:
        Store the difference of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

`sinter(self, keys, *args)`:
        Return the intersection of sets specified by ``keys``

`sinterstore(self, dest, keys, *args)`:
        Store the intersection of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

`sismember(self, name, value)`:
        Return a boolean indicating if ``value`` is a member of set ``name``

`smembers(self, name)`:
        Return all members of the set ``name``

`smove(self, src, dst, value)`:
        Move ``value`` from set ``src`` to set ``dst`` atomically

`spop(self, name)`:
        Remove and return a random member of set ``name``

`srandmember(self, name, number=None)`:
        If ``number`` is None, returns a random member of set ``name``.
        If ``number`` is supplied, returns a list of ``number`` random
        memebers of set ``name``. Note this is only available when running
        Redis 2.6+.

`srem(self, name, *values)`:
        Remove ``values`` from set ``name``

`sunion(self, keys, *args)`:
        Return the union of sets specified by ``keys``

`sunionstore(self, dest, keys, *args)`:
        Store the union of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

`sscan(self, name, cursor=0, match=None, count=None)`:
        Incrementally return lists of elements in a set. Also return a cursor
        indicating the scan position.
        ``match`` allows for filtering the keys by pattern
        ``count`` allows for hint the minimum number of returns

`sscan_iter(self, name, match=None, count=None)`:
        Make an iterator using the SSCAN command so that the client doesn't
        need to remember the cursor position.
        ``match`` allows for filtering the keys by pattern
        ``count`` allows for hint the minimum number of returns

#有序set操作
`zadd(self, name, *args, **kwargs)`:
        Set any number of score, element-name pairs to the key ``name``. Pairs
        can be specified in two ways:
        As `*args`, in the form of: score1, name1, score2, name2, ...
        or as `**kwargs`, in the form of: name1=score1, name2=score2, ...
       The following example would add four values to the 'my-key' key:
        redis.zadd('my-key', 1.1, 'name1', 2.2, 'name2', name3=3.3, name4=4.4)
        

`zcard(self, name)`:
        Return the number of elements in the sorted set ``name``

`zcount(self, name, min, max)`:
        Returns the number of elements in the sorted set at key ``name`` with
        a score between ``min`` and ``max``.

`zincrby(self, name, value, amount=1)`:
        Increment the score of ``value`` in sorted set ``name`` by ``amount``
        return self.execute_command('ZINCRBY', name, amount, value)

`zinterstore(self, dest, keys, aggregate=None)`:
        Intersect multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.


`zlexcount(self, name, min, max)`:
        Return the number of items in the sorted set ``name`` between the
        lexicographical range ``min`` and ``max``.

`zrange(self, name, start, end, desc=False, withscores=False,
               score_cast_func=float)`:
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.
       ``start`` and ``end`` can be negative, indicating the end of the range.
       ``desc`` a boolean indicating whether to sort the results descendingly
       ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs
       ``score_cast_func`` a callable used to cast the score return value

`zrangebylex(self, name, min, max, start=None, num=None)`:
        Return the lexicographical range of values from sorted set ``name``
        between ``min`` and ``max``.
        If ``start`` and ``num`` are specified, then return a slice of the
        range.

`zrevrangebylex(self, name, max, min, start=None, num=None)`:
        Return the reversed lexicographical range of values from sorted set
        ``name`` between ``max`` and ``min``.
        If ``start`` and ``num`` are specified, then return a slice of the
        range.

`zrangebyscore(self, name, min, max, start=None, num=None,
                      withscores=False, score_cast_func=float)`:
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.
        If ``start`` and ``num`` are specified, then return a slice
        of the range.
        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs
        `score_cast_func`` a callable used to cast the score return value

```
        
# 当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员
# 对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大
 
# 参数：
    # name，redis的name
    # min，左区间（值）。 + 表示正无限； - 表示负无限； ( 表示开区间； [ 则表示闭区间
    # min，右区间（值）
    # start，对结果进行分片处理，索引位置
    # num，对结果进行分片处理，索引后面的num个元素
 
# 如：
    # ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
    # r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
 
# 更多：
    # 从大到小排序
    # zrevrangebylex(name, max, min, start=None, num=None)

```

`zrank(self, name, value)`:
        Returns a 0-based value indicating the rank of ``value`` in sorted set
        ``name``

`zrem(self, name, *values)`:
        Remove member ``values`` from sorted set ``name``

`zremrangebylex(self, name, min, max)`:
        Remove all elements in the sorted set ``name`` between the
        lexicographical range specified by ``min`` and ``max``.
        Returns the number of elements removed.


`zremrangebyrank(self, name, min, max)`:
        Remove all elements in the sorted set ``name`` with ranks between
        ``min`` and ``max``. Values are 0-based, ordered from smallest score
        to largest. Values can be negative indicating the highest scores.
        Returns the number of elements removed

`zremrangebyscore(self, name, min, max)`:
        Remove all elements in the sorted set ``name`` with scores
        between ``min`` and ``max``. Returns the number of elements removed.

`zrevrange(self, name, start, end, withscores=False,
                  score_cast_func=float)`:
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.
        ``start`` and ``end`` can be negative, indicating the end of the range.
        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs
        ``score_cast_func`` a callable used to cast the score return value


`zrevrangebyscore(self, name, max, min, start=None, num=None,
                         withscores=False, score_cast_func=float)`:
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.
        If ``start`` and ``num`` are specified, then return a slice
        of the range.
        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs
        ``score_cast_func`` a callable used to cast the score return value

`zrevrank(self, name, value)`:
        Returns a 0-based value indicating the descending rank of
        ``value`` in sorted set ``name``

`zscore(self, name, value)`:
        Return the score of element ``value`` in sorted set ``name``

`zunionstore(self, dest, keys, aggregate=None)`:
        Union multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.

#订阅发布
PubSub类创建Publish/Subscribe对象, 实现订阅发布功能. 两个主要的方法publish和subscribe.
比RabbitMQ简单多了.

PubSub provides publish, subscribe and listen support to Redis channels.
After subscribing to one or more channels, the listen() method will block
until a message arrives on one of the subscribed channels. That message
will be returned and it's safe to start listening again.

`pubsub(self, **kwargs)`:
        Return a Publish/Subscribe object. With this object, you can
        subscribe to channels and listen for messages that get published to
        them.
`publish(self, channel, message)`:
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.

`subscribe(self, *args, **kwargs)`:
        Subscribe to channels. Channels supplied as keyword arguments expect
        a channel name as the key and a callable as the value. A channel's
        callable will be invoked automatically when a message is received on
        that channel rather than producing a message via ``listen()`` or
        ``get_message()``.

