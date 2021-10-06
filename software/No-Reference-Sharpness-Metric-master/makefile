TARGET := jnb
CC1 := clang++ -v
CC2 := g++ -v

SRC_DIR   = src
OBJ_DIR   = obj
BIN_DIR   = bin

INCLUDE_DIR = -Iinclude -I/usr/include/
#INCLUDE_DIR = -Iinclude -I/usr/local/include/
LIBRARY_DIR = -Llib -L/usr/local/lib/
LIBRARIES = -lopencv_core -lopencv_highgui -lopencv_imgproc
LD_FLAGS = -O2 -Wall -stdlib=libc++ -std=c++11

SOURCES := $(wildcard $(SRC_DIR)/*.cpp)
SOURCES := $(filter-out $(wildcard $(SRC_DIR)/test*.cpp), $(SOURCES))
OBJECTS := $(SOURCES:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

$(BIN_DIR)/$(TARGET): $(OBJECTS)
	@$(CC2) -o $@ $(LD_FLAGS) $(LD_FLAGS) $(LIBRARY_DIR) $(LIBRARIES)  $(OBJECTS)
	@echo "Linked OK"

$(OBJECTS): $(OBJ_DIR)/%.o : $(SRC_DIR)/%.cpp
	@$(CC1) $(CFLAGS) -c $< -o $@ $(INCLUDE_DIR) $(LD_FLAGS)
	@echo "Compiled OK"

.PHONEY: clean
clean:
	rm -f $(OBJECTS)
	
.PHONEY: remove
remove: clean
	@$(rm) $(BIN_DIR)/$(TARGET)

.PHONEY: list
list:
	@echo $(SOURCES)
