cwd=$(pwd)
COSMOS_ROOT="$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )/.."
COSMOS_CODE_ROOT="$COSMOS_ROOT/code"
UNCRUSTIFY_ROOT_PATH="$COSMOS_ROOT/third_party/uncrustify"
UNCRUSTIFY="$UNCRUSTIFY_ROOT_PATH/build/uncrustify"
UNCRUSTIFY_CONFIG_PATH="$UNCRUSTIFY_ROOT_PATH/../uncrustify.cfg"

error_code=0
total=0
error=0

echo """
###########################
# Building uncrustify ... #
###########################
"""
# tmp="$(mktemp tmp.XXXXXXXXXX)"
# cd $UNCRUSTIFY_ROOT_PATH
# rm -rf build
# mkdir build
# cd build
# cmake .. > $tmp
# cmake --build . > $tmp
# rm -rf $tmp

echo """
########################
# Formatting files ... #
########################
"""
cd $COSMOS_CODE_ROOT
for cpp_file in `find . -name '*.cpp'`
do
    # remove the output file if it already existed.
    rm -f $cpp_file.uncrustify
    if [[ "$?" -ne 0 ]]; then
        echo "# Failed to remove file: \`$COSMOS_CODE_ROOT/$cpp_file\`.\n"
    fi;

    u=$("$UNCRUSTIFY" -q -c "$UNCRUSTIFY_CONFIG_PATH" "$COSMOS_CODE_ROOT/$cpp_file")
    total=$(($total+1))

    if [[ "$?" -ne 0 ]]; then
        echo "# Failed to create uncrustify file: \`$COSMOS_CODE_ROOT/$cpp_file\`.\n"
    fi;
done

echo """
#######################
# Comparing files ... #
#######################
"""
cd $COSMOS_CODE_ROOT
for cpp_file in `find . -name '*.cpp'`
do
    d=$(diff "$cpp_file" "$cpp_file.uncrustify")

    if [[ "$?" -ne 0 ]]; then
        echo "# The \`$COSMOS_CODE_ROOT/$cpp_file\` is not passed"
        error=$(($error+1))
    fi;
done

cd "$cwd"

if [ $error_code != 0 ]; then
    exit 1
elif [ $error != 0 ]; then
    echo "Failed. $error/$total error(s) generated."
    exit 1
else
    echo "Passed."
fi;
