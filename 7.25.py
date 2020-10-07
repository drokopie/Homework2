#Dominic okopie 1672505
using namespace std;

void ExactChange(int userTotal, vector<int>& coinVals) {
    coinVals.push_back(userTotal / 100);
    userTotal %= 100;
    coinVals.push_back(userTotal / 25);
    userTotal %= 25;
    coinVals.push_back(userTotal / 10);
    userTotal %= 10;
    coinVals.push_back(userTotal / 5);
    userTotal %= 5;
    coinVals.push_back(userTotal);
}

int main() {
    vector<int> coins;
    int value;
    cin >> value;
    if (value <= 0) {
        cout << "no change" << endl;
    } else {
        ExactChange(value, coins);
        if (coins[0] != 0)
            cout << coins[0] << " " << (coins[0] == 1 ? "dollar" : "dollars") << endl;
        if (coins[1] != 0)
            cout << coins[1] << " " << (coins[1] == 1 ? "quarter" : "quarters") << endl;
        if (coins[2] != 0)
            cout << coins[2] << " " << (coins[2] == 1 ? "dime" : "dimes") << endl;
        if (coins[3] != 0)
            cout << coins[3] << " " << (coins[3] == 1 ? "nickel" : "nickels") << endl;
        if (coins[4] != 0)
            cout << coins[4] << " " << (coins[4] == 1 ? "penny" : "pennies") << endl;
    }
    return 0;
}