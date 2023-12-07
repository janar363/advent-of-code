# include <iostream>
# include <vector>
# include <string>

using namespace std;

int main(){
    string lineInp;
    long long total_sum = 0;
    int count = 0;

    vector<string> numbers;
    numbers.push_back("one");
    numbers.push_back("two");
    numbers.push_back("three");
    numbers.push_back("four");
    numbers.push_back("five");
    numbers.push_back("six");
    numbers.push_back("seven");
    numbers.push_back("eight");
    numbers.push_back("nine");


    while(getline(cin, lineInp)){
        if(lineInp.empty()) {
            break;
        }

        long long first_digit = -1, last_digit = -1;
        for(int i=0; i < lineInp.length(); i++){
            char ch = lineInp[i];

            if(ch >= '0' && ch <= '9'){
                last_digit = ch-'0';

                if(first_digit == -1)
                    first_digit = ch-'0';
            } else {

                for(int number_idx=0; number_idx < numbers.size(); number_idx++){

                    if(lineInp.substr(i, numbers[number_idx].length()) == numbers[number_idx]) {
                        

                        last_digit = number_idx+1;

                        if(first_digit == -1)
                            first_digit = number_idx+1;
                    }
                }

            }
        }

        if(first_digit == -1)
            cout << "No digit in string\n";
        total_sum += first_digit * 10 + last_digit;
        cout << "current 2 digit number = " << first_digit << last_digit << endl;
        cout << "current total sum = " << total_sum << endl;

    }
    cout << "total sum = " << total_sum << endl;

}