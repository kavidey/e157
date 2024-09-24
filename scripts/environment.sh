export RF_SCRIPTS_PATH="$(dirname "$0")";

alias ltspice_to_s1p='$RF_SCRIPTS_PATH/ltspice_to_s1p.sh';

alias ltspice_to_s1p_all="find . -name '*.txt' -exec $RF_SCRIPTS_PATH/ltspice_to_s1p.sh {} \;";