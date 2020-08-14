import random
from util import Stack, Queue  # These may come in handy


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add Users
        for i in range(1, num_users + 1):
            self.add_user(i)

        # Create friendships
        # to create N of random friendships
        # create a list with all friendship combinations
        # shuffle the list, then get the first N elements from the list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        # create a queue
        q = Queue()
        # enqueue a path to user_id
        q.enqueue([user_id])
        # create a dictionary for key value pairs
        visited = {}  # Note that this is a dictionary, not a set
        # while the queue is not empty..
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the vertex from the end of the path
            v = path[-1]
            # check to see if it's been visited, and if not
            if v not in visited:
                if v is not user_id:
                    # mark it as such
                    visited[v] = path
                # enqueue a path to all its neighbors
                for neighbor in self.friendships[v]:
                    if neighbor not in visited:
                        # make a copy of the path
                        copy = path.copy()
                        # append the neighbor
                        copy.append(neighbor)
                        # enqueue the copy
                        q.enqueue(copy)



        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
