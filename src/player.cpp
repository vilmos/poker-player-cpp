#include "player.h"


const char *Player::VERSION = "hellraiser\n";

int Player::betRequest(json::Value game_state) {

	if (game_state.GetType() == json::ValueType::ObjectVal && game_state.HasKey("minimum_raise")) {
		json::Value out = game_state["minimum_raise"];
		if (out.GetType() == json::ValueType::IntVal) {
			return out.ToInt();

		}
	}
	return 10;
}

void Player::showdown(json::Value game_state) {
}
