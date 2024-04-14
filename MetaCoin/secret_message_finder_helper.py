path_to_log_file = r"C:\Custom Apps\MultiMC\instances\Fabulously Optimized 5.8.0-beta.10\.minecraft\logs\latest.log"
parsed_output = r"OUTPUTS/output.txt"

def parse_log():
    log_file = open(path_to_log_file, "r", errors='ignore')
    output_file = open(parsed_output, "w")

    for line in log_file.readlines():
        if "MetaCoin" in line:
            output_file.write(line[line.index("[CHAT] ") + 7:])

    log_file.close()
    output_file.close()

