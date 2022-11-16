#!/usr/bin/env ruby
# A egular expression to parse textme log files
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
