/*
This file implements a LRU cache using C++ STL list and unordered_map. The list is used to prioritise the items from LRU to MRU. LRU items are at the end of the list whilst
MRU items are at the begining of the list. The unordered_map is used to map the key of an item to a key,value pair that is inside the aforementioned list. The list acts as a 
doubly linked list because in C++ you can iterate through a list forward and backwards. It also hides the pointer logic that is required to insert and remove items to and from
a doubly linked list by using list::splice() function.
*/

#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
    private:
    int cap;
    list<pair<int, int>> li; // This keeps track of the key,value pairs with most recently used at the beginning and least at the end
    unordered_map<int, list<pair<int, int>>::iterator> hmap; // This is our cache, maps key to somewhere on "li" (i.e. a pair of key, value)
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        // If key isn't in hashmap remove it
        if (hmap.find(key) == hmap.end()) return -1;
        
        // Otherwise, place the (key, value) pair at the start of li and return value 
        li.splice(li.begin(), li, hmap[key]);
        return hmap[key]->second;
    }
    
    void put(int key, int value) {
        // If key is in hashmap, update value and return
        if (get(key) != -1)
        {
            hmap[key]->second = value;
            return;
        }
        
        // If cache full
        if (hmap.size() == cap)
        {
            // Get the key to delete from the back of LI
            int del = li.back().first;
            li.pop_back(); // Remove from LI
            hmap.erase(del); // Delete from cache
        }
        
        // Place new key at the front, and enter into hashmap
        li.emplace_front(key, value);
        hmap[key] = li.begin();
    }
};