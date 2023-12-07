# include <iostream>
# include <vector>
# include <set>
using namespace std;

int main(){
    vector<string> engine;

    string line;

    int r=0;
    long long total_sum = 0;
    while(getline(cin, line)){
        if(line.empty()) {
            break;
        }

        r++;
        engine.push_back(line);

    }

    for(int i=0; i<r; i++){
        for(int j=0; j<engine[i].size(); j++){
            // vector<int> indices;
            vector<long long> adj_nums;
            vector<pair<int, int> > idx_pairs;
            long long gear_ratio = 0;

            if(engine[i][j] == '*'){
                
                cout << "entered if for i = " << i << " j = " << j << "\n";
                if(i != 0 && j != 0 && engine[i-1][j-1] >= '0' && engine[i-1][j-1] <= '9'){
                    int temp = j-1;
                    while(temp >= 0 && engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    long long num = 0;
                    
                    pair<int, int> idx_ = make_pair(i-1, temp);
                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(make_pair(i-1, temp));
                    
                    while(engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                        num = num * 10ll + (long long)engine[i-1][temp] - '0';
                        temp++;
                    }
                    adj_nums.push_back(num);
                    }
                    cout << "exit 1\n";
                } 
                if(i != 0 && engine[i-1][j] >= '0' && engine[i-1][j] <= '9'){
                    int temp = j;
                    while(temp >= 0 && engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i-1, temp);

                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(idx_);

                        long long num = 0;
                        while(engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i-1][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                    }
                    cout << "exit 2\n";
                } 
                if(i != 0 && j != engine[i].size()-1 && engine[i-1][j+1] >= '0' && engine[i-1][j+1] <= '9'){
                    int temp = j+1;
                    while(temp >= 0 && engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i-1, temp);

                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(idx_);
                        long long num = 0;
                        while(engine[i-1][temp] >= '0' && engine[i-1][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i-1][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                    }
                    cout << "exit 3\n";
                } 
                if(j != 0 && engine[i][j-1] >= '0' && engine[i][j-1] <= '9'){
                    cout << "entered exit 4\n";
                    int temp = j-1;
                    while(temp >= 0 && engine[i][temp] >= '0' && engine[i][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i, temp);

                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        cout << "enterd exit 4 inner\n";
                        idx_pairs.push_back(idx_);
                        cout << "x = " << idx_.first << " y = " << idx_.second << endl;
                        long long num = 0;
                        while(engine[i][temp] >= '0' && engine[i][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                    }
                    cout << "adj c at exit 4 = " << adj_nums.size() << endl;
                    cout << "exit 4\n";
                } 
                if(j != engine[i].size()-1 && engine[i][j+1] >= '0' && engine[i][j+1] <= '9'){
                    cout << "entered exit 5\n";
                    int temp = j+1;
                    while(temp >= 0 && engine[i][temp] >= '0' && engine[i][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    
                    pair<int, int> idx_ = make_pair(i, temp);
                    
                    
                    int id_size = idx_pairs.size();
                    if(id_size != 0){
                        cout << "xx = " << idx_pairs[id_size-1].first << " yy = " << idx_pairs[id_size-1].second << endl;
                        cout << "x = " << idx_.first << " y = " << idx_.second << endl;
                    }
                    // cout << "id_size == 0 || (idx_pairs[id_size-1].first != idx_.first && idx_pairs[id_size-1].second != idx_.second) = " << ((idx_pairs[id_size-1].first != idx_.first && idx_pairs[id_size-1].second != idx_.second)) << endl;
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        cout << "entered exit 5 inner\n";
                        idx_pairs.push_back(idx_);
                        cout << "x = " << idx_.first << " y = " << idx_.second << endl;
                        long long num = 0;
                        while(engine[i][temp] >= '0' && engine[i][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                    }
                    cout << "adj c at exit 5 = " << adj_nums.size() << endl;
                        cout << "exit 5\n";
                } 
                if(i != r-1 && j != 0 && engine[i+1][j-1] >= '0' && engine[i+1][j-1] <= '9'){
                    int temp = j-1;
                    while(temp >= 0 && engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i+1, temp);
                    cout << "x = " << idx_.first << " y = " << idx_.second << endl;
                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(idx_);
                        long long num = 0;
                        while(engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i+1][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                        }
                        cout << "exit 6\n";
                } 
                if(i != r-1 && engine[i+1][j] >= '0' && engine[i+1][j] <= '9'){
                    int temp = j;
                    while(temp >= 0 && engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i+1, temp);
                    
                    int id_size = idx_pairs.size();
                    
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(idx_);
                        long long num = 0;
                        while(engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                            num = num * 10ll + (long long)engine[i+1][temp] - '0';
                            temp++;
                        }
                        adj_nums.push_back(num);
                    }
                        cout << "exit 7\n";
                } 
                if(i != r-1 && j != engine[i].size()-1 && engine[i+1][j+1] >= '0' && engine[i+1][j+1] <= '9'){
                    int temp = j+1;
                    while(temp >= 0 && engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                        temp--;
                    }
                    temp++;
                    pair<int, int> idx_ = make_pair(i+1, temp);
                    int id_size = idx_pairs.size();
                    if(id_size == 0 || (idx_pairs[id_size-1].first != idx_.first || idx_pairs[id_size-1].second != idx_.second)){
                        idx_pairs.push_back(idx_);
                    long long num = 0;
                    while(engine[i+1][temp] >= '0' && engine[i+1][temp] <= '9'){
                        num = num * 10ll + (long long)engine[i+1][temp] - '0';
                        temp++;
                    }
                    adj_nums.push_back(num);
                    }
                    cout << "exit 8\n";
                }
                cout << "exiting if\n";
            }
            
            if(adj_nums.size() == 2){
                gear_ratio = adj_nums[0] * adj_nums[1];
            }

            // cout << "adj_numbser count = " << adj_nums.size() << endl;

            total_sum += gear_ratio;

            cout << "total sum for i = " << i << " j = " << j << " sum = " << total_sum << endl;
            
        }



    }

    cout << "total_sum = " << total_sum << endl;


}


// for(auto id: indices){
//                 // cout << "enterd for i = " << i << " id = " << id << endl;
//                 // if(i == 0 && id == 2){
//                 //     cout << "i != r-1 && id != engine[i].size()-1 && engine[i+1][id+1] < '0' && engine[i+1][id+1] > '9' && engine[i+1][id+1] != '.' = " << (i != r-1 && id != engine[i].size()-1 && (engine[i+1][id+1] < '0') << endl;
//                 //     // && engine[i+1][id+1] < '0' && engine[i+1][id+1] > '9' && engine[i+1][id+1] != '.'
//                 // }
//                 if(i != 0 && id != 0 && (engine[i-1][id-1] < '0' || engine[i-1][id-1] > '9') && engine[i-1][id-1] != '.'){
//                     total_sum += num;break; 
//                 } else if(i != 0 && (engine[i-1][id] < '0' || engine[i-1][id] > '9') && engine[i-1][id] != '.'){
//                     total_sum += num;break;
//                 } else if(i != 0 && id != engine[i].size()-1 && (engine[i-1][id+1] < '0' || engine[i-1][id+1] > '9') && engine[i-1][id+1] != '.'){
//                     total_sum += num;break;
//                 } else if(id != 0 && (engine[i][id-1] < '0' || engine[i][id-1] > '9') && engine[i][id-1] != '.'){
//                     total_sum += num;break;
//                 } else if(id != engine[i].size()-1 && (engine[i][id+1] < '0' || engine[i][id+1] > '9') && engine[i][id+1] != '.'){
//                     total_sum += num;break;
//                 } else if(i != r-1 && id != 0 && (engine[i+1][id-1] < '0' || engine[i+1][id-1] > '9') && engine[i+1][id-1] != '.'){
//                     total_sum += num;break;
//                 } else if(i != r-1 && (engine[i+1][id] < '0' || engine[i+1][id] > '9') && engine[i+1][id] != '.'){
//                     total_sum += num;break;
//                 } else if(i != r-1 && id != engine[i].size()-1 && (engine[i+1][id+1] < '0' || engine[i+1][id+1] > '9') && engine[i+1][id+1] != '.'){
//                     total_sum += num;break;
//                 }
//                 cout << "total_sum after i = " << i << " id = " << id << " sum = " << total_sum << endl;
//             }  

/*
467..114..
...*......
..35..633.
......#...
617*1.....
.....+.58.
..592.....
......755.
...$.*....
.664.598..
*/