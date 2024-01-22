import argparse
import json


def flatten_json(y):
    out = {}
 
    def flatten(x, name=''):
 
        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:
 
            for a in x:
                flatten(x[a], name + a + '_')
 
        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:
 
            i = 0
 
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
 
    flatten(y)
    return out


def flatten_items_json(items, output_filename_base):
    i = 0
    for item in items:
        # execute flatten json
        item_output = flatten_json(item)
        print("flatten-json: item_output = %s" % (item_output))
        print("flatten-json: item_output type = %s" % (type(item_output)))

        # serialize json with indentation
        item_output_json = json.dumps(item_output)

        # write flattened json file
        i += 1
        item_output_filename = output_filename_base+"-"+str(i)+"-flattened.json"
        with open(item_output_filename, "w") as item_output_file:
            item_output_file.write(item_output_json)
        item_output_file.close()
        print("flatten-json: wrote output file = %s" % (item_output_filename))

    return True


if __name__ == '__main__':
    # read arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input-filename", required=True, help="Input JSON dataset filename.")
    ap.add_argument("-o", "--output-filename-base", required=True, help="Output JSON dataset filename base.")
    args = vars(ap.parse_args())
    print("flatten-json: args = %s" % (args))

    # load json file
    input_filename = args['input_filename']
    with open(input_filename, 'r') as input_file:
        input = json.load(input_file)
    input_file.close()
    print("flatten-json: input = %s" % (input))
    print("flatten-json: input type = %s" % (type(input)))

    # execute flatten items json
    items = input["data"]["plays"]["items"]
    output_filename_base = args['output_filename_base']
    success = flatten_items_json(items, output_filename_base)
    if success:
        print("flatten-json: successfully flattened %d items." % (len(items)))
    else:
        print("flatten-json: failed to flatten %d items." % (len(items)))

