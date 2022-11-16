#!/usr/bin/env ruby
# A egular expression that must match only capiltal lettersr
puts ARGV[0].scan(/[A-Z]/).join
