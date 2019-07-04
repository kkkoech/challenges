function pizza_slice(cuts)
    return  convert(Int,(1+cuts*(cuts+1)/2))
end

print(pizza_slice(2), "\n") 
print(pizza_slice(3), "\n") 
print(pizza_slice(4))
