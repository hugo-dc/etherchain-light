import argparse, json, sys, binascii

parser = argparse.ArgumentParser(description='Preload a Geth genesis with contract accounts')

parser.add_argument('--template', type=str, nargs='?',
                            help='path to the genesis source template')
parser.add_argument('--faucet-address', type=str, nargs='?',
                            help='faucet address')
parser.add_argument('--private-key', type=str, nargs='?',
                            help='faucet private key')
parser.add_argument('--block-count', type=int, nargs='?',
                            help='number of blocks to search last transactions')

parse_args = parser.parse_args()

template = parse_args.template
faucet_address = parse_args.faucet_address
private_key = parse_args.private_key
block_count = parse_args.block_count

try:
  with open(template) as f:
    template = f.read().replace('{privateKey}', private_key)
    template = template.replace('{faucetAddress}', faucet_address)
    template = template.replace('{blockCount}', str(block_count))
    print(template)
except Exception as e:
  print(e)
  sys.exit(1)

