#include "player.h"


const char *Player::VERSION = "hellraiser";

int Player::betRequest(json::Value game_state) {
	if (game_state.HasKey("minimum_raise")) {
		json::Value out = game_state["minimum_raise"];
		return out.ToInt();
	}
	return 10;
}

void Player::showdown(json::Value game_state) {
}
