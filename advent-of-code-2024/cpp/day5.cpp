# include <iostream>
# include <fstream>
# include <vector>
# include <unordered_map>
# include <sstream>

# define NUM(s) ((s[0] - '0') * 10 + (s[1] - '0'))

using namespace std;

vector<string> split(string str, char at){
    vector<string> tokens;
    string token;
    istringstream stream(str);

    while(getline(stream, token, at)) tokens.push_back(token);

    return tokens;
}

vector<int> getNewOrdering(vector<int> & ordering, unordered_map<int, vector<int> > & rules){
    vector<int> newOrdering = ordering;
    for(int page1=0;page1 < ordering.size(); page1++){
        int count = 0;
        for(int page2=0; page2 < ordering.size(); page2++){
            if(page1 == page2) continue;

            if(find(rules[ordering[page1]].begin(), rules[ordering[page1]].end(), ordering[page2]) != rules[ordering[page1]].end()) {
                count++;
            }
        }
        newOrdering[ordering.size()-count-1] = ordering[page1];
    }
    return newOrdering;
}

int main(){
    ifstream file("../input");

    string str;
    unordered_map<int, vector<int> > rules;
    vector<vector<int> > orderings;

    while(file >> str){
        if(str.length() == 5){
            rules[NUM(str)].push_back(NUM(str.substr(3, 2)));
        } else {
            vector<int> ordering;

            for(auto s: split(str, ',')){
                ordering.push_back(NUM(s));
            }
            orderings.push_back(ordering);
        }
    }
    
    int part1 = 0;
    int part2 = 0;

    for(auto ordering: orderings){
        bool rightOrdering = true;
        for(int page1=0;page1 < ordering.size(); page1++){
            
            for(int page2=page1+1; page2 < ordering.size(); page2++){
                if(find(rules[ordering[page1]].begin(), rules[ordering[page1]].end(), ordering[page2]) == rules[ordering[page1]].end()) {
                    rightOrdering=false;
                    vector<int> newOrdering = getNewOrdering(ordering, rules);
                    part2 += newOrdering[newOrdering.size() / 2];
                    break;
                }
            }
            if(!rightOrdering) break;
        }

        if(rightOrdering) part1 += ordering[ordering.size() / 2];
    }
    
    cout << "part1 : " << part1 << endl;
    cout << "part2 : " << part2 << endl;

}