# include <iostream>
# include <vector>
# include <set>
# include <unordered_map>


using namespace std;

int main(){
    vector<string> pile;

    string line;


    long long total_sum = 0;
    int id=1;
    unordered_map<int, int> cards_count;
    while(getline(cin, line)){
        cards_count[id]++;
        if(line.empty()) {
            break;
        }

        pile.push_back(line);

        int i = 0;

        while(line[i++] != ':');
            i++;

        bool completed_win_nums = false;
        set<int> win_nums;
        vector<int> my_nums;

        for(; i<line.size(); i++){
            
            if(line[i] >= '0' && line[i] <= '9'){
                long long num = 0;
                while(i < line.size() && line[i] != ' '){
                    num = num * 10ll + (line[i]-'0');
                    i++;
                }

                if(!completed_win_nums)
                    win_nums.insert(num);
                else 
                    my_nums.push_back(num);
            }

            if(line[i] == '|')
                completed_win_nums = true;
        }

        
        
        long long cur_points = 0;
        cout << "my nums : ";
        for(auto num: my_nums){
            cout << num << " ";
            if(win_nums.find(num) != win_nums.end()){
                cur_points++;
            }

        }
        cout << endl;

        for(int k=0; k<cards_count[id]; k++){
        for(int j=id+1; j<=id+cur_points; j++){
            cards_count[j]++;
        }
        }
        
        id++;
    }

    for (auto const& [key, val] : cards_count)
    {
        if(key == id) continue;
        cout << "card " << key << " count = " << val << endl;
        total_sum += val;
    }
    cout << "total_sum = " << total_sum << endl;
}