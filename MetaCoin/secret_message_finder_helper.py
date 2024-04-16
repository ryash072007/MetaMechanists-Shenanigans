path_to_log_file = r"C:\Custom Apps\MultiMC\instances\Fabulously Optimized 5.8.0-beta.10\.minecraft\logs\latest.log"
full_parsed_output = r"MetaCoin\full_parsed.txt"
set_parsed_output = r"MetaCoin\set_parsed.txt"

parsed_output_set = set()

def parse_log():
    log_file = open(path_to_log_file, "r", errors='ignore')
    output_file = open(full_parsed_output, "w")

    for line in log_file.readlines():
        if "MetaCoin" in line and line.rstrip().endswith("."):
            line_data = line[line.index("[CHAT] ") + 7:]
            output_file.write(line_data)
            parsed_output_set.add(line_data)

    parsed_output_list = list(parsed_output_set)
    with open(set_parsed_output, "w") as f:
        for item in parsed_output_list:
            f.write(item)
    
    log_file.close()
    output_file.close()

parse_log()


