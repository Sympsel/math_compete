classdef Binom
    properties
        n  % 实验次数
        p  % 每次成功的概率
        E
        Var
        Std
        coef
        skew
        kurt
    end

    methods
        function obj = Binom(n, p)
            if ~isscalar(n) || n <= 0 || floor(n) ~= n
                error('实验次数 n 必须为正整数');
            end
            if p < 0 || p > 1
                error('成功概率 p 必须在 [0, 1] 区间内');
            end
            obj.n = n;
            obj.p = p;
            obj.E = obj.expectation();
            obj.Var = obj.variance();
            obj.Std = obj.std_dev();
            obj.coef = obj.coef_variation();
            obj.skew = obj.skewness();
            obj.kurt = obj.kurtosis(false);
        end

        function val = pmf(obj, k)
            if k < 0 || k > obj.n
                val = 0;
            else
                val = nchoosek(obj.n, k) * (obj.p ^ k) * ((1 - obj.p) ^ (obj.n - k));
            end
        end

        function val = cdf(obj, k)
            if k < 0
                val = 0;
            elseif k >= obj.n
                val = 1;
            else
                val = 0;
                for i = 0:k
                    val = val + obj.pmf(i);
                end
            end
        end

        function val = expectation(obj)
            val = obj.n * obj.p;
        end

        function val = variance(obj)
            val = obj.n * obj.p * (1 - obj.p);
        end

        function val = std_dev(obj)
            val = sqrt(obj.variance());
        end

        function val = coef_variation(obj)
            mu = obj.E;
            if mu ~= 0
                val = obj.Std / mu;
            else
                val = inf;
            end
        end

        function val = raw_moment(obj, k)
            val = 0;
            for i = 0:obj.n
                val = val + (i ^ k) * obj.pmf(i);
            end
        end

        function val = central_moment(obj, k)
            mu = obj.E;
            val = 0;
            for i = 0:obj.n
                val = val + ((i - mu) ^ k) * obj.pmf(i);
            end
        end

        function val = quantile(obj, q)
            if q < 0 || q > 1
                error('q 必须在 [0, 1] 区间内');
            end
            cum = 0;
            for i = 0:obj.n
                cum = cum + obj.pmf(i);
                if cum >= q
                    val = i;
                    return;
                end
            end
            val = obj.n;
        end

        function val = skewness(obj)
            val = (1 - 2 * obj.p) / sqrt(obj.n * obj.p * (1 - obj.p));
        end

        function val = kurtosis(obj, excess)
            if nargin < 2
                excess = false;
            end
            ex_k = (1 - 6 * obj.p * (1 - obj.p)) / (obj.n * obj.p * (1 - obj.p));
            if excess
                val = ex_k;
            else
                val = ex_k + 3;
            end
        end

        function str = summary(obj)
            str = sprintf(['二项分布：X~B(n=%d, p=%.3f)\n' ...
                           '期望: %.4f\n方差: %.4f\n变异系数: %.4f\n' ...
                           '偏度: %.4f\n峰度: %.4f'], ...
                           obj.n, obj.p, obj.E, obj.Var, obj.coef, obj.skew, obj.kurt);
        end
    end
end
