# include<iostream>
# include<vector>
# include<map>
# include<set>

using namespace std;

int main(){
    long long times;
    long long distances;

    string line;
    int count = 0;
    while(getline(cin, line)){

        if(line.empty()) {
            break;
        }
        cout << line << endl;

        int i=0; 

        while(i<line.size() && line[i++] != ':');
        i++;
        cout << "i = " << i << endl;
        long long num = 0;
        for(;i<line.size(); i++){
            
            if(!isdigit(line[i])) continue;

            num = num * 10ll + (line[i]-'0');

                
        }
        if(count == 0) {times = num; cout << "times = " << times << endl;}
        else {distances = num; cout << "distances = " << distances << endl;}

        count++;
    }
    cout << "got input\n";
    long long total = 1;
    bool found = false;
    
    long long speed = 1;
    long long time = 0;
    cout << "distance = " << distances << endl;
    cout << "time = " << times << endl;
    while(!found){
        time = distances / speed;

        if(distances % speed != 0) time++;
        // cout << "found time"
        if(time+speed < times) {found = true; break;}
        speed++;
        // cout << "not found \n";
    }
    cout << "lowest time = " << time << "for speed = " << speed << endl;

    // for(int i=0; i<times.size(); i++){
    //     long long time = times[i];
    //     long long distance = distances[i];
    //     long long win_count = 0;
    //     for(long long j=0; j<=time; j++){
    //         long long speed = j;

    //         long long dist = (time-speed) * speed;

    //         if(dist > distance) win_count++;

    //     }
    //     // cout << "current count"
    //     total *= win_count; 

    // }

    cout << "total ways win = " << times - (2*speed-1) << endl;
}

/*
Time:      15 
Distance:  40  
*/