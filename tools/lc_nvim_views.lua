-- View commands can also be loaded into an attached workspace without reopening its files.
local script = debug.getinfo(1, "S").source:sub(2)
local root = vim.fs.dirname(vim.fs.dirname(script))

local function close_views()
  for _, win in ipairs(vim.api.nvim_tabpage_list_wins(0)) do
    if vim.w[win].lc_workspace_view then
      vim.api.nvim_win_close(win, false)
    end
  end
end

-- Route CLI problem switches back through the normal workspace editor.
if _G.LCOpen and _G.LCOpen ~= _G.LCOpenWithViews then
  local open_problem = _G.LCOpen
  _G.LCOpenWithViews = function(path)
    close_views()
    return open_problem(path)
  end
  _G.LCOpen = _G.LCOpenWithViews
end

local function show_view(path, title)
  if vim.o.columns < 20 or vim.o.lines < 8 then
    vim.notify("Phóng to pane bằng Ctrl+Space rồi z để mở phần xem.", vim.log.levels.WARN)
    return
  end
  local ok, lines = pcall(vim.fn.readfile, path)
  if not ok then
    vim.notify(tostring(lines), vim.log.levels.ERROR)
    return
  end
  close_views()
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)
  vim.bo[buf].bufhidden = "wipe"
  vim.bo[buf].modified = false
  vim.bo[buf].readonly = true
  vim.bo[buf].modifiable = false
  vim.bo[buf].syntax = vim.filetype.match({ filename = path }) or ""

  local width = math.min(96, vim.o.columns - 4)
  local height = math.max(1, math.min(#lines, vim.o.lines - 4))
  local win = vim.api.nvim_open_win(buf, true, {
    relative = "editor",
    width = width,
    height = height,
    row = math.floor((vim.o.lines - height - 2) / 2),
    col = math.floor((vim.o.columns - width - 2) / 2),
    style = "minimal",
    border = "rounded",
    title = title,
  })
  vim.w[win].lc_workspace_view = true
  vim.wo[win].wrap = true
  vim.wo[win].linebreak = true
  local function close()
    vim.api.nvim_win_close(win, false)
  end
  for _, key in ipairs({ "q", "<Esc>" }) do
    vim.keymap.set("n", key, close, { buffer = buf, desc = "Đóng phần xem LeetCode" })
  end
end

vim.keymap.set("n", "<leader>ls", function()
  close_views()
  local path = vim.api.nvim_buf_get_name(0)
  if not path:match("/solution%.py$") and not path:match("/solution%.sql$") then
    vim.notify("Mở bản nháp hoặc lời giải workspace trước.", vim.log.levels.WARN)
    return
  end
  local result = vim.system(
    { root .. "/bin/lc", "reference", "--path", path },
    { cwd = root, text = true }
  ):wait(5000)
  if result.code ~= 0 then
    vim.notify(vim.trim(result.stderr or ""), vim.log.levels.WARN)
    return
  end
  show_view(vim.trim(result.stdout or ""), " Lời giải tham khảo ")
end, { desc = "LeetCode xem lời giải tham khảo" })

vim.keymap.set("n", "<leader>lh", function()
  show_view(root .. "/practice/workspace-shortcuts.md", " Phím tắt LeetCode ")
end, { desc = "LeetCode bảng phím tắt" })
