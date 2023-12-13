# include<iostream>
# include<vector>
# include<fstream>
# include<algorithm>

using namespace std;

vector<vector<string> > notes; 

void fetch_input(){
    std::ifstream file("day13.txt");

    string line;
    long long line_c=0;
    
    // get input
    vector<string> new_notes;
    while(getline(file, line)){

        if(line.length() == 0){
            notes.push_back(new_notes);
            new_notes.clear();
        } else {
            new_notes.push_back(line);
        }
        
    }
    notes.push_back(new_notes);
}

vector<string> rotate_notes(vector<string> note){
    vector<string> rotated_note;
    for(int j=0; j<note[0].size(); j++){
        string str = "";
        for(int i=note.size()-1; i>=0; i--){
            str += note[i][j];
        }
        rotated_note.push_back(str);
    }

    return rotated_note;
}

vector<long long> compare_splits(vector<string> & a, vector<string> & b){
    vector<long long> diff(3, 0);
    for(int i=0; i<min(a.size(), b.size()); i++){
        for(int j=0; j<a[0].length(); j++){
            if(a[i][j] != b[i][j]) {diff[0]++; diff[1] = i, diff[2] = j;}
        }
    }
    return diff;
}

vector<vector<string> > split_note(vector<string>  note, long long r){
    vector<vector<string> > split(2);
    int s = r < note.size()/2 ? 0 : r;
    int l = r <= note.size()/2 ? note.size()-1 : r-1;

    string str = "";
    for(int i=r-1; i>=0; i--){

        split[0].push_back(note[i]);
    } 


    for(int i=r; i<note.size(); i++){
        split[1].push_back(note[i]);

    }


    return split;
}


long long get_perfect_reflection_count(vector<string> note, int part=1){
    long long cur_ans = 0;

    for(long long i=1; i<note.size(); i++){
        vector<vector<string> > ab = split_note(note, i);

        vector<long long> diff = compare_splits(ab[0], ab[1]);
        
        if(part == 2 && diff[0] == 1) {
            cur_ans = i; break;
        } else if(part == 1 && diff[0] == 0){
            cur_ans = i; break;
        }

    }

    
    return cur_ans;
}

int main(){

    fetch_input();

    long long hc = 0, vc = 0, total_count = 0;

    for(int i=0; i<notes.size(); i++){
        vector<long long> cur_ans(2, 0);

        hc += get_perfect_reflection_count(notes[i]);

        vc += get_perfect_reflection_count(rotate_notes(notes[i]));

    }

    
    
    cout << "vc = " << vc << " hc = " << hc << endl;
    cout << vc + 100ll * hc << endl; 
    
    hc = 0, vc = 0, total_count = 0;

    for(int i=0; i<notes.size(); i++){
        vector<long long> cur_ans(2, 0);

        hc += get_perfect_reflection_count(notes[i], 2);

        vc += get_perfect_reflection_count(rotate_notes(notes[i]), 2);

    }
    cout << vc + 100ll * hc << endl; 
 

    
}
