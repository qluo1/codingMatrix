voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    ret = {}
    for i in voting_data:
        data = i.split()
        ret[data[0]] = [int(data[i]) for i in range(3,len(data))]
    return ret

def create_voting_ref():
    """ """
    ret = {}
    for i in voting_data:
        data = i.split()
        ret[(data[0],data[1],data[2])] = [int(data[i]) for i in range(3,len(data))]
    return ret


## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    vot_a,vot_b = voting_dict[sen_a],voting_dict[sen_b]

    return sum([a*b for (a,b) in zip(vot_a,vot_b)])

## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    sen_vot = voting_dict[sen]
    most = -len(sen_vot)
    cand = ''

    for i in voting_dict.keys():
        if i != sen:
            res =  policy_compare(sen,i,voting_dict)
            if  res > most:
                most = res
                cand = i
    return cand


## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
   
    sen_vot = voting_dict[sen]
    most = policy_compare(sen,sen,voting_dict)
    cand = ''

    for i in voting_dict:
            res =  policy_compare(sen,i,voting_dict)
            # print res,most,i
            if  res < most:
                most = res
                cand = i
    return cand

## Task 5

most_like_chafee    = most_similar('Lincoln',create_voting_dict())

least_like_santorum = least_similar('Santorum',create_voting_dict())


# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    # print [[a*b for (a,b) in zip(voting_dict[sen],voting_dict[k])] for k in sen_set]
    vots = [sum([a*b for (a,b) in zip(voting_dict[sen],voting_dict[k])]) for k in sen_set]
    return sum(vots)/(len(vots)*1.0)


demo_sent_set = {i[0] for i in create_voting_ref() if i[1] =='D'}

demo_avg ={i:find_average_similarity(i,demo_sent_set,create_voting_dict()) for i in demo_sent_set}

most_average_Democrat = max(demo_avg,key=demo_avg.get) # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    return [sum(i) * 1.0 /len(sen_set)  for i in zip(*[voting_dict[i] for i in sen_set])]

avg_demo = find_average_record(demo_sent_set,create_voting_dict())

demo_avg_2 = {i: sum([a*b for (a,b) in zip(create_voting_dict()[i],avg_demo)]) for i in demo_sent_set}
average_Democrat_record = max(demo_avg_2,key=demo_avg_2.get) # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    return ('...', '...')

