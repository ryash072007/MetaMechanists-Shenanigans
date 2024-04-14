path_to_log_file = r"C:\Custom Apps\MultiMC\instances\Fabulously Optimized 5.8.0-beta.10\.minecraft\logs\latest.log"
parsed_output = r"MetaCoin\output.txt"

parsed_output_set = set()

def parse_log():
    log_file = open(path_to_log_file, "r", errors='ignore')
    output_file = open(parsed_output, "w")

    for line in log_file.readlines():
        if "MetaCoin" in line:
            line_data = line[line.index("[CHAT] ") + 7:]
            output_file.write(line_data)
            parsed_output_set.add(line_data)

    log_file.close()
    output_file.close()

parse_log()