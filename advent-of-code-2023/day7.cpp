# include<iostream>
# include<vector>
# include<algorithm>
#include <fstream>


using namespace std;

unordered_map<char, int> scores;

int get_hand_idx(vector<int> type){
    sort(type.begin(), type.end(), greater<int>());

    if(type[0] == 5) return 0;
    if(type[0] == 4) return 1;
    if(type[0] == 3 && type[1] == 2) return 2;
    if(type[0] == 3 && type[1] == 1) return 3;
    if(type[0] == 2 && type[1] == 2) return 4;
    if(type[0] == 2 && type[1] == 1) return 5;
    return 6;
}

bool compare(pair<string, long long> left, pair<string, long long> right){
    if(scores[left.first[0]] != scores[right.first[0]]) return scores[left.first[0]] > scores[right.first[0]];
    if(scores[left.first[1]] != scores[right.first[1]]) return scores[left.first[1]] > scores[right.first[1]];
    if(scores[left.first[2]] != scores[right.first[2]]) return scores[left.first[2]] > scores[right.first[2]];
    if(scores[left.first[3]] != scores[right.first[3]]) return scores[left.first[3]] > scores[right.first[3]];
    return scores[left.first[4]] > scores[right.first[4]];
}

int main(){

    std::ifstream file("aoc_py/input");

    scores['A'] = 14;
    scores['K'] = 13;
    scores['Q'] = 12;
    scores['J'] = 1;
    scores['T'] = 10;
    scores['9'] = 9;
    scores['8'] = 8;
    scores['7'] = 7;
    scores['6'] = 6;
    scores['5'] = 5;
    scores['4'] = 4;
    scores['3'] = 3;
    scores['2'] = 2;

    vector<vector<pair<string, long long> > > hands(7);

    string line;
    long long rank = 0;
    while(getline(file, line)){
        
        if(line.empty()) {
            break;
        }

        
        int i=0;
        int unique_c = 0;
        long long num = 0;
        string hand="";
        vector<int> type(5, 0);
        vector<int> chars(91, 0); 
        // get hand info 
        for(;i<line.size(); i++){
            
            if(line[i] == ' ') break;

            chars[line[i]]++;
            hand += line[i];
        }
        
        // getting card with max count and count of card J
        int max_char = 0;
        int max_c = 0;
        int j_c = 0;
        for(int j=65; j<=90; j++){

            if(j != 'J' && chars[j] > max_c) {
                max_c = chars[j];
                max_char = j;
            } else if(j != 'J' && chars[j] == max_c && scores[(char)j] > scores[(char)max_char]){
                max_c = chars[j];
                max_char = j;
            }else if(j == 'J'){
                j_c = chars[j];
            }

            
        }
        
        for(int j=48; j<=57; j++){
            
            if(chars[j] > max_c) {
                max_c = chars[j];
                max_char = j;
            } else if(chars[j] == max_c && scores[(char)j] > scores[(char)max_char]){
                max_c = chars[j];
                max_char = j;
            }
        }

        // cout << "max char before = " << (char)(max_char) << endl;

        //  adding J count to card with max count other than J
        chars[max_char] += j_c;
        chars['J'] = 0;

        // identifying type of hand
        unique_c = 0;
        for(int j=65; j<=90; j++){
            if(chars[j] != 0)
                type[unique_c++] = chars[j];

            
        }
        
        for(int j=48; j<=57; j++){
            if(chars[j] != 0)
                type[unique_c++] = chars[j];
        }
        
        // cout << "type = " << type[0] << " " << type[1] << " " << type[2] << " " << type[3] << " " << type[4] << endl;
        int idx = get_hand_idx(type);
        
        i++;
        for(;i<line.size(); i++){
            if(!isdigit(line[i])) continue;

            num = num * 10ll + (line[i]-'0');
        }
        //  adding hand and bid info to the identified hand type
        hands[idx].push_back(make_pair(hand, num));
        rank++;
    }

    // cout << "total rank = " << rank << endl;; 
    long long total = 0;
    for(int i=0; i<hands.size(); i++){
        // cout << "hand " << i+1 << " : " << endl;
        sort(hands[i].begin(), hands[i].end(), compare);
        for(auto h: hands[i])
            total += h.second * rank--;
    }

    cout << "total score = " << total << endl;
}