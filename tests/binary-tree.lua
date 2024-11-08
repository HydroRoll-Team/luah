-- The Computer Language Benchmarks Game
-- http://benchmarksgame.alioth.debian.org/
-- contributed by Mike Pall

local function BottomUpTree(item, depth)
    if depth > 0 then
      local i = item + item
      depth = depth - 1
      local left, right = BottomUpTree(i-1, depth), BottomUpTree(i, depth)
      return { item, left, right }
    else
      return { item }
    end
  end
  
  local function ItemCheck(tree)
    if tree[2] then
      return tree[1] + ItemCheck(tree[2]) - ItemCheck(tree[3])
    else
      return tree[1]
    end
  end
  
  local N = 10 -- input argument
  local mindepth = 4
  local maxdepth = mindepth + 2
  if maxdepth < N then maxdepth = N end
  
  do
    local stretchdepth = maxdepth + 1
    local stretchtree = BottomUpTree(0, stretchdepth)
    print("stretch tree of depth", stretchdepth, "check: ", ItemCheck(stretchtree))
  end
  
  local longlivedtree = BottomUpTree(0, maxdepth)
  
  for depth=mindepth,maxdepth,2 do
    local iterations = 2 ^ (maxdepth - depth + mindepth)
    local check = 0
    for i=1,iterations do
      check = check + ItemCheck(BottomUpTree(1, depth)) +
              ItemCheck(BottomUpTree(-1, depth))
    end
    print(iterations*2, "trees of depth", depth, "check: ", check)
  end
  
  print("long lived tree of depth", maxdepth, "check:", ItemCheck(longlivedtree))