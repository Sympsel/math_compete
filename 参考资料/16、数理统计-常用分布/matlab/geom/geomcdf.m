function c = geomcdf(prob, k)
%GEOM_CDF 几何分布的累积分布函数 P(X <= k)

    validate_geom(prob);

    if k < 1
        c = 0;
    else
        c = 1 - (1 - prob)^k;
    end
end
