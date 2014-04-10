#include<iostream>
#include "json.h"
#include "player.h"

using namespace std;

int main(int argc, char *argv[]) {
	if (argv[1]) {
		string action = argv[1];

		string game_state_json;
		if (action == "bet_request") {
			if (argv[2]) {
				game_state_json = argv[2];
			}
			else {
				cin >> game_state_json;
			}

			json::Value game_state = json::Deserialize(game_state_json);
			cout << Player::betRequest(game_state);
		}
		else if (action == "showdown") {
			cin >> game_state_json;

			json::Value game_state = json::Deserialize(game_state_json);
			Player::showdown(game_state);
		}
		else if (action == "version") {
			cout << Player::VERSION;
		}
	}
	return 0;
}
