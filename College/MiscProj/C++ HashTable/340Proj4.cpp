#include <iostream>
#include <list>
#include <string>
#include <algorithm>
#include <fstream>
#include <cctype>
#include <cstdlib>
using namespace std;

struct Words{//struct of each word to be inputted.
    string word;
    int steps;     
    int occurrences; 

    Words(const string& w, int s){ // Constructor
        word = w;
        steps = s;
        occurrences = 1;
    }
};

class HashTable{
    static const int tableSize = 500;//hash table size
    list<Words> table[tableSize];

public:
int HashCode (const string &str){
    int h = 0;
    for (size_t i = 0; i < str.size(); ++i)
    h = h * 31 + static_cast<int>(str[i]);
    return abs(h % tableSize);
}
int NewHashCode(const string &str) {//experiment usage
    int h = 0;
    for (int i = 0; i < str.size(); i++){
        h += static_cast<int>(str[i]);
    }
    return abs(h % tableSize);
}
void Insert(string word){
    for (size_t i = 0; i < static_cast<long int>(word.length()); ++i){
        word[i] = std::tolower(static_cast<unsigned char>(word[i]));//make words lowercase 
    }//make all lowercase 
    int index = HashCode(word);
    int positionInList = 0;
    for (auto& entry : table[index]) {
        if (entry.word == word) {
            entry.occurrences++; //word found!
            entry.steps += (positionInList + 1); //step counter
            return;
        }
        positionInList++;
    }

    table[index].insert(table[index].end(), Words(word, positionInList + 1));//word not found? append to linked list
    }

    void ToCSV(const string& filename) const{
        ofstream file(filename);
        if (!file) {
            cerr << "Error opening file!" << endl;
            return;
        }
        for (int i = 0; i < tableSize; ++i) {//loop through and add each word to the CSV file
            for (const auto& entry : table[i]) {
                file << entry.word << "," << entry.steps << "," << entry.occurrences << "\n";
            }
        }
        file.close();
        cout << "CSV: " << filename << endl;
    }
    
};


int main(){
    HashTable myTable;
    ifstream inputFile("C:\\Users\\Zayne\\projects\\LittleWomen.txt");//change as needed, my environment required this

    if (!inputFile) {
        cerr << "Error opening file!" << endl;
        return 1; // error ==> exit
    }
    int wordCount = 0;
    string word;
    while (inputFile >> word) { //Reads words
        myTable.Insert(word); //Insert said words
        wordCount++;
    }

    inputFile.close();

    cout << wordCount;//print total number of words, useful for error checking ==186609
    myTable.ToCSV("output500.CSV");
return 0;
}