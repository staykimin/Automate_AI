from kimin.core_server import Set_Server

config_path = "kimin/config.min"

x = Set_Server(config_path)
server = x.Server()

if __name__ == '__main__':
	x.Routes(server)
	x.Run(server)