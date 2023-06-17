#! /usr/bin/env bash
# Some checksum representation for the tag annotations.
[ -n "${1}" ] || exit 2
path="${1}"
[ -f "${path}" ] || exit 1
printf "  + artifact:%s:\n" "${path}"
printf "    * %s:" "blake3"
b3sum "${path}" | cut -f 1 -d ' ' | tr -d "\n"
printf "\n    * %s:" "crc32"
crc32 "${path}" | tr -d "\n"
printf "\n    * %s:" "entropy"
ent -t "${path}" | grep 1 | cut -f 3 -d ',' | tr -d "\n"
printf "\n    * %s:(" "file"
file "${path}" | cut -f 2- -d ':' | cut -c 2- | tr -d "\n"
printf ")"
printf "\n    * %s:" "hex32"
xxd -ad -ps -g 32 -c 32 -len 32 "${path}" | tr -d "\n"
printf "\n    * %s:" "md5"
md5sum "${path}" | cut -f 1 -d ' '
for h in sha sha256 sha384 sha512
do 
    printf "    * %s:" "${h}"
    ${h}sum "${path}" | cut -f 1 -d ' '
done
printf "    * %s:" "tlsh"
tlsh -f "${path}" | cut -f 1 | tr -d "\n"
printf "\n"

