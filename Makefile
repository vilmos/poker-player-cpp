
CC=g++

CFLAGS=-c -std=c++11
SRC=src
TGT=obj

SOURCES = $(wildcard $(SRC)/*.cpp)

OBJS = $(addprefix $(TGT)/, $(notdir $(SOURCES:.cpp=.o)))

all: player

player: $(OBJS)
	$(CXX) $(OBJS) -o $@
	
$(TGT)/%.o: $(SRC)/%.cpp
	$(CXX) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(TGT)/* player
