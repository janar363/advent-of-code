# include <iostream>
# include <vector>

using namespace std;

int main(){
    string game;

    long long id_c = 0;
    long long power = 0;
    int id = 1;
    while(getline(cin, game)){
        if(game.empty()) {
            break;
        }

        long long red=0, green=0, blue=0;
        int i = 0;

        while(game[i++] != ':');
        i++;
        for(; i<game.length(); i++){
            
            
            if(game[i] >= '0' && game[i] <= '9' && game[i+1] != ':'){
                long long num = 0;
                while(game[i] != ' '){
                    num = num * 10ll + (game[i]-'0');
                    i++;
                }


                if(game[i+1] == 'r'){
                    cout << "enterd into red";
                    red = max(red, num);
                } else if(game[i+1] == 'g'){
                    green = max(green, num);
                } else if(game[i+1] == 'b'){
                    blue = max(blue, num);
                }
            }
        }

    cout << "red = " << red << " green " << green << " blue = " << blue << endl; 
        if(red <= 12 && green <= 13 && blue <= 14){
            id_c += id;
        }
        id++;
        power += red * green * blue;
    }

    cout <<  "total id_c = " << id_c << endl;
    cout << "power = " << power << endl;
}
