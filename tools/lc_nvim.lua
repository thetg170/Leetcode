-- Loaded only in the workspace editor. Existing LazyVim and kata mappings stay active.
local script = debug.getinfo(1, "S").source:sub(2)
local root = vim.fs.dirname(vim.fs.dirname(script))
local lc = root .. "/bin/lc"

local server = vim.v.servername
vim.api.nvim_create_autocmd("VimLeave", { once = true, callback = function()
  vim.fn.serverstop(server)
  vim.uv.fs_rmdir(vim.fs.dirname(server))
end })

function _G.LCOpen(path)
  local mode = vim.api.nvim_get_mode().mode
  if (mode ~= "n" and mode ~= "nt") or vim.fn.getcmdwintype() ~= "" then
    return "Finish the current Neovim action first."
  end
  if vim.bo.buftype == "terminal" then
    local code_window = vim.w.lc_result_source
    if not code_window or not vim.api.nvim_win_is_valid(code_window)
        or vim.api.nvim_win_get_tabpage(code_window) ~= vim.api.nvim_get_current_tabpage()
        or vim.bo[vim.api.nvim_win_get_buf(code_window)].buftype ~= "" then
      return "Close the terminal result and choose the problem again."
    end
    vim.api.nvim_set_current_win(code_window)
  end
  if vim.api.nvim_buf_get_name(0) == path then
    return ""
  end
  local ok, err = pcall(vim.cmd.edit, { args = { path }, mods = { hide = true } })
  return ok and "" or tostring(err)
end

local function background(args)
  vim.system(vim.list_extend({ lc }, args), { text = true }, function(result)
    if result.code ~= 0 then
      vim.schedule(function()
        vim.notify(vim.trim((result.stderr or "") .. (result.stdout or "")), vim.log.levels.WARN)
      end)
    end
  end)
end

local function check(action)
  local path = vim.api.nvim_buf_get_name(0)
  if not path:match("/solution%.py$") and not path:match("/solution%.sql$") then
    vim.notify("Open a workspace solution first.", vim.log.levels.WARN)
    return
  end
  local saved, failure = pcall(vim.cmd.update)
  if not saved then
    vim.notify(tostring(failure), vim.log.levels.ERROR)
    return
  end
  local code_window = vim.api.nvim_get_current_win()
  vim.cmd("botright new")
  vim.w.lc_result_source = code_window
  vim.cmd.resize(math.max(1, math.min(10, math.floor(vim.o.lines / 3))))
  vim.fn.jobstart({ lc, action, "--path", path }, { term = true, cwd = root })
  vim.cmd.stopinsert()
  vim.keymap.set("n", "q", "<cmd>close<cr>", { buffer = true, desc = "Close local result" })
end

vim.keymap.set("n", "<leader>lt", function() check("test") end, { desc = "LeetCode test" })
vim.keymap.set("n", "<leader>lr", function() check("run") end, { desc = "LeetCode run example" })
vim.keymap.set("n", "<leader>ll", function() background({ "lang", "toggle" }) end,
  { desc = "LeetCode switch VI/EN" })
vim.keymap.set("n", "<leader>ln", function() background({ "next", "--no-attach" }) end,
  { desc = "LeetCode next problem" })
vim.keymap.set("n", "<leader>lp", function()
  local command = { "tmux" }
  if vim.env.LC_TMUX_SOCKET then
    vim.list_extend(command, { "-L", vim.env.LC_TMUX_SOCKET })
  end
  vim.list_extend(command, { "display-popup", "-EE", "-t", vim.env.TMUX_PANE,
    "-w", "85%", "-h", "75%", lc, "pick" })
  vim.system(command, { text = true }, function(result)
    if result.code ~= 0 then
      vim.schedule(function()
        vim.notify(vim.trim(result.stderr or ""), vim.log.levels.WARN)
      end)
    end
  end)
end, { desc = "LeetCode pick problem" })

dofile(root .. "/tools/lc_nvim_views.lua")
