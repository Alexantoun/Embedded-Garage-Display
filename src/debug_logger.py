class DebugLogger:
    output_file = open('debug_output', 'w')

    @staticmethod
    def write_debug(debug_calling_class: str, message: str):
        DebugLogger.output_file.write(debug_calling_class+'\t'+message+'\n')

    @staticmethod
    def close():
        DebugLogger.output_file.close()
