import routes


if __name__ == '__main__':

    try:
        routes.server()

    except KeyboardInterrupt:
        print('Stop signal received')

    except SystemExit as e:
        print(e.code)

    except Exception:
        print('!!!UNHANDLED EXCEPTION!!!')
