#!/usr/bin/python3

import sys
import socket
import struct

class client_unix_socket:
    __slots__ = ("_socketfile", "_socket")

    def __init__(self, socketfile):
        self._socketfile = socketfile
        self._socket = None

    def socket(self):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self):
        try:
            self._socket.connect(self._socketfile)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"\"{self._socketfile}\" socket file doesn't exist")

    def recv(self, bufsize):
        return self._socket.recv(bufsize)

class crti_data:
    __slots__ = ("_line", "_result", "_exec_time")

    def __init__(self):
        self._line = None
        self._result = None
        self._exec_time = None

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, line):
        self._line = line

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    @property
    def exec_time(self):
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        self._exec_time = exec_time

class crti_client:
    __slots__ = ("_cl_args")

    def __init__(self, cl_args):
        self._cl_args = cl_args

    def start(self):
        client_sock = client_unix_socket("crti.sock")

        client_sock.socket()
        client_sock.connect()

        while True:
            try:
                buffer = client_sock.recv(1024)
            except KeyboardInterrupt:
                print('\n', end='')

                break

            if not buffer:
                break

            deserialized_data = self._deserialize(buffer)

            self._show_crti_data(deserialized_data)

    @staticmethod
    def _deserialize(buffer):
        deserialized_data = crti_data()
        offset = 0

        # "line" field
        line_size = struct.unpack_from("N", buffer, offset)[0]

        offset += struct.calcsize("N")
        deserialized_data.line = struct.unpack_from(
            f"{line_size}s", buffer, offset)[0].decode("UTF-8")
        offset += line_size


        # "result" field
        result_size = struct.unpack_from("N", buffer, offset)[0]

        offset += struct.calcsize("N")
        deserialized_data.result = struct.unpack_from(
            f"{result_size}s", buffer, offset)[0].decode("UTF-8")
        offset += result_size


        # "exec_time" field
        deserialized_data.exec_time = struct.unpack_from(
            "d", buffer, offset)[0]
        offset += struct.calcsize("d")

        return deserialized_data

    def _show_crti_data(self, deserialized_data):
        print(f"line : {deserialized_data.line}\n"
              f"result : {deserialized_data.result}\n"
              f"execution time : {deserialized_data.exec_time} µs\n"
              "----------------------------------------------------",
              end="\n\n")

def parse_command_line_args():
    import argparse

    parser = argparse.ArgumentParser()
    mandatory_grp = parser.add_argument_group(
        "exclusive mandatory arguments") \
    .add_mutually_exclusive_group(required=True)

    mandatory_grp.add_argument("-l",
                               "--local",
                               action="store_true",
                               help="client for local only")
    # mandatory_grp.add_argument("-r",
    #                            "--remote",
    #                            action="store_true",
    #                            help="client for remote "
    #                            "[to use with -i, -p options]")

    # conditional_required_grp = parser.add_argument_group(
    #     "conditional arguments required")
    # remote_opt_is_set = any(v in ["-r", "--remote"] for v in sys.argv)

    # conditional_required_grp.add_argument("-i",
    #                                       "--ip",
    #                                       type=str,
    #                                       required=remote_opt_is_set,
    #                                       help="ip for client remote")
    # conditional_required_grp.add_argument("-p",
    #                                       "--port",
    #                                       type=int,
    #                                       required=remote_opt_is_set,
    #                                       help="port for client remote")

    return parser.parse_args()


if __name__ == "__main__":
    cl_args = parse_command_line_args()

    try:
        # if cl_args.remote:
        #     raise NotImplementedError("remote crti client not "
        #                               "implemented yet")

        client = crti_client(cl_args)

        client.start()
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(-1)
    except:
        print(f"unknown exception caught: {sys.exc_info()[1]}",
              file=sys.stderr)
        sys.exit(-1)
    else:
        sys.exit(0)
