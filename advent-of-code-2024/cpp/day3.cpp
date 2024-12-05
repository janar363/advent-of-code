# include <iostream>
# include <fstream>

using namespace std;

long long checkMul(string & inp, int i){

    if(inp[i+1] == 'u' && inp[i+2] == 'l' && inp[i+3] == '('){
        int n1 = 0, n2 = 0;
        i += 4;

        while(isnumber(inp[i])) n1 = n1 * 10 + (inp[i++] - '0');
        if(inp[i] == ',') i += 1;
        while(isnumber(inp[i])) n2 = n2 * 10 + (inp[i++] - '0');

        if(inp[i] == ')') return n1 * n2;
    }

    return 0;
}

int main(){
    ifstream file("../input");

    char ch; 
    string inp="";

    while(file >> ch){
        inp += ch;
    }

    long long part1 = 0, part2 = 0;    

    bool do_ = true;

    for(int i=0; i<inp.size(); i++){
        if(inp[i] == 'm') part1 += checkMul(inp, i);

        if(do_ && inp[i] == 'm') part2 += checkMul(inp, i);

        if(do_ && i + 6 < inp.length() && inp.substr(i, 7) == "don't()") do_ = false;

        if(!do_ && i+3 < inp.length() && inp.substr(i, 4) == "do()") do_ = true;
    }

    cout << "part1 : " << part1 << endl;
    cout << "part2 : " << part2 << endl;
}